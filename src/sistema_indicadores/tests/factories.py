import factory

from sistema_indicadores.models import Organization


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    name = factory.Faker("name")
