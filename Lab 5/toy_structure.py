from app import ma


class ToyStructure(ma.Schema):
    class Meta:
        fields = ('id', 'size', 'age')
