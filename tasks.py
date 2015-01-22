"""

"""

from invoke import task, run

bin_dir = 'django_inventory/bin'
main = '{bin_dir}/django-inventory.py'.format(
    bin_dir=bin_dir,
)

@task
def server():
    """ Starts the django web server """

    cmd = '{main} runserver'.format(
        main=main,
    )

    run(cmd)

@task
def task(command):
    """ Run any command from `django-inventory.py` using this task

    :param cmd:
    :return:
    """

    cmd = '{main} {cmd}'.format(
        main=main,
        cmd=command
    )

    run(cmd)

@task
def help():
    """ Shows the help menu for `django-inventory.py` """

    run(main)