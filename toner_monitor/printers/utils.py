import asyncio
from pysnmp.hlapi.asyncio import ContextData, SnmpEngine, CommunityData, UdpTransportTarget, ObjectType, ObjectIdentity, get_cmd

# Function to query SNMP and fetch toner levels
async def snmp_query(ip_address):
    toner_oids = {
        'black': '1.3.6.1.2.1.43.11.1.1.9.1',  # Black toner OID
        'cyan': '1.3.6.1.2.1.43.11.1.1.9.2',  # Cyan toner OID
        'magenta': '1.3.6.1.2.1.43.11.1.1.9.3',  # Magenta toner OID
        'yellow': '1.3.6.1.2.1.43.11.1.1.9.4',  # Yellow toner OID
    }
    
    toner_levels = {}

    for color, oid in toner_oids.items():
        # Await the creation of the transport target
        transport_target = await UdpTransportTarget.create((ip_address, 161))  # Use the provided IP address
        
        error_indication, error_status, error_index, var_binds = await get_cmd(
            SnmpEngine(),
            CommunityData('swedint'),
            transport_target,
            ContextData(),
            ObjectType(ObjectIdentity(oid))  # Fetching toner level for each color
        )

        if error_indication or error_status:
            print(f"Error for {color}: {error_indication}")
            toner_levels[color] = None  # Mark toner level as None if query failed
        else:
            for var_bind in var_binds:
                toner_levels[color] = int(var_bind[1])  # Save toner level
            print(f"{color.capitalize()} toner level: {toner_levels[color]}%")

    return toner_levels

# Run the asyncio query and return the toner levels
def get_printer_toner_level(ip_address):
    return asyncio.run(snmp_query(ip_address))
