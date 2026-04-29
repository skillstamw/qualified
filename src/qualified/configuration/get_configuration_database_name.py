# pylint: disable=line-too-long, W0718, W0719
r"""
# Specification get_configuration_database_name 

## About
- Author(s): Mats Wallden
- Inception: 2026-04-29T12:33:44.535Z
- Language: Python
- Part of: qualified
- key words: configuration, database

## Summary
returns a file name for a configuration database

## Input argument(s)
- tag (str, optional): descriptive tag used in the file name. Defaults to "default".


## Returns argument(s)
- str: configuration database file name 

## Error handling
- TypeError: if the input tag is not str
- ValueError: if the input tag contains dot character

## Testing

## Style
Linting was performed using pylint TODO 

## Instructions for use
### example 
TODO consider how to make these tests.. 
./src/qualified/configuration/get_configuration_database_name_test.py #TODO implement
"""

from uuid import UUID
from uuid import uuid4
from hydra.assert_type import assert_type
from hydra.assert_member_is_not_in_container import assert_member_is_not_in_container
from mindmeld.mindmeld.output.get_time_stamp import get_time_stamp

def get_configuration_database_name(tag:str="default")->str:
    """returns a file name for a configuration database

    Args:
        tag (str, optional): descriptive tag used in the file name. Defaults to "default".

    Returns:
        str: configuration database file name 
    """
    location_id=UUID("c13c593e-db0a-47e1-83b4-b120ca967b8b")
    assert_type(value=tag,expected_type=str,
                location_id=UUID("f8ff8a81-c0b5-4352-b2cd-986a31707020"),
                additional="the tag for the configration database file name was not a string")
    assert_member_is_not_in_container(member='.',
                                      container=tag,
                                      location_id=UUID("54ef7acc-2c8a-4db4-bfce-0db8d3e8ca36"),
                                      additional=f"expected tag not to contain dot character when using {__file__} at location {location_id}. Consider if the file name is corrupt or being misused")
    return f"configuration_{tag}_{get_time_stamp()}_{str(uuid4()).replace('-','_')}.db"

if __name__=="__main__":
    pass
