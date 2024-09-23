from django.db.models import *


class ProductBranch(Model):
    name = CharField(max_length=20, null=False, blank=False, unique=True)
    description = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"ProductBranch(name={self.name})"


class ProductType(Model):
    name = CharField(max_length=25, null=False, blank=False)
    branch_type = ManyToManyField(ProductBranch, blank=True, related_name="product_types")
    description = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"ProductType(name={self.name})"


class ProductDetail(Model):
    name = CharField(max_length=25, null=False, blank=False)
    product_type = ManyToManyField(ProductType, blank=True, related_name="products")
    detailed_info = TextField(null=True, blank=True)
    more_info = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Product(name={self.name})"
