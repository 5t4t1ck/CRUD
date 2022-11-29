import click

@click.group()
def clients():
    """Manejar el ciclo de vida de los clientes"""
    pass

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Crear un nuevo cliente"""


@clients.command()
@click.pass_context
def list(ctx):
    """Lista de todos los clientes"""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Actualiza un cliente"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Eliminar un cliente"""
    pass


all = clients
