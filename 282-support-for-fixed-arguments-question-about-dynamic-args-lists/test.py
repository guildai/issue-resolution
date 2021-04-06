import argparse
import pyobjconfig as poc


class SubThing1(poc.ConfigurableObject):
    class config(poc.PydanticBaseModel):
        var: int = 8


class SubThing2(poc.ConfigurableObject):
    class config(poc.PydanticBaseModel):
        iable: int = 5


class Thing(poc.ConfigurableObject):
    class config(poc.PydanticBaseModel):
        width: float = 10.5

    sub_thing = poc.ConfigurableSwitch(
        {
            "thing1": SubThing1,
            "thing2": SubThing2,
        }
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    Thing.argparse_setup(ap)
    args = ap.parse_args()
    print("parse args: %s" % args)
    thing = Thing.argparse_create(args.__dict__)
    print("thing.config: %s" % thing.config)
    print("thing.sub_thing: %s" % type(thing.sub_thing).__name__)
    if isinstance(thing.sub_thing, SubThing1):
        print("thing.sub_thing.config.var: %s" % thing.sub_thing.config.var)
    elif isinstance(thing.sub_thing, SubThing2):
        print("thing.sub_thing.config.iable: %s" % thing.sub_thing.config.iable)
    else:
        assert False, type(thing.sub_thing)
