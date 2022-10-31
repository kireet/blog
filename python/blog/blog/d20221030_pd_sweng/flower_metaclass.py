class FlowerMetaclass(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        """
        Adds class level properties with value=field name. Useful for use with data frames.
        """
        # cls = FlowerMetaclass.__new__(mcs, name, bases, namespace, **kwargs)
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        for p in namespace["__annotations__"]:
            setattr(cls, p, p)
        return cls
