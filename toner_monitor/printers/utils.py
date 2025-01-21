import asyncio
from pysnmp.hlapi.asyncio import ContextData, SnmpEngine, CommunityData, UdpTransportTarget, ObjectType, ObjectIdentity, get_cmd

async def snmp_query(ip_address):
    # Await the creation of the transport target
    transport_target = await UdpTransportTarget.create((ip_address, 161))  # Use the provided IP address
    
    error_indication, error_status, error_index, var_binds = await get_cmd(
        SnmpEngine(),
        CommunityData('swedint'),
        transport_target,
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))  # Or other OID related to toner level
    )

    if error_indication:
        print(f"Error: {error_indication}")
        return None
    else:
        for var_bind in var_binds:
            print(f"{var_bind}")
        # You can modify this to extract the toner level if needed
        return 100  # Example: Return a mock toner level for now

def get_printer_toner_level(ip_address):
    # Run the asyncio loop to get the toner level
    return asyncio.run(snmp_query(ip_address))
