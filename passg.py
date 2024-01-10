import click
import string
import random

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(no_args_is_help=True, context_settings=CONTEXT_SETTINGS)
@click.option('--num_pass', show_default=True, default=1, help='set number of passwords to generate')
@click.option('-l', '--length', type=click.IntRange(1,128), show_default=True, help='set length of generated password')
@click.option('-up', '--upper', is_flag=True, show_default=True, default=False, help="include uppercase letters")
@click.option('-lo', '--lower', is_flag=True, show_default=True, default=False, help="include uppercase letters")
@click.option('-n', '--num', is_flag=True, show_default=True, default=False, help="include numbers")
@click.option('-s', '--special', is_flag=True, show_default=True, default=False, help="include special ascii characters")
@click.option('-e', '--extended', is_flag=True, show_default=True, default=False, help="include extended ascii characters")
@click.option('-p', '--punct', is_flag=True, show_default=True, default=False, help="include punctuation")
@click.option('-q', '--quotes', is_flag=True, show_default=True, default=False, help="include quotes")
@click.option('-d', '--dashes', is_flag=True, show_default=True, default=False, help="include dashes and slashes")
@click.option('-m', '--math', is_flag=True, show_default=True, default=False, help="include math symbols")
@click.option('-b', '--braces', is_flag=True, show_default=True, default=False, help="include braces")
@click.option('-x', '--exclude', multiple=True, help='items to exclude, case sensitive, surround in ""')
@click.version_option(version='1.0.0', prog_name='passg')

def cli(num_pass, length, upper, lower, num, special, extended, punct, quotes, dashes, math, braces, exclude):
    value_pool = []
    values_to_exclude = []

    if upper:
        value_pool.extend(string_to_chars(string.ascii_uppercase))
    if lower:
        value_pool.extend(string_to_chars(string.ascii_lowercase))
    if num:
         for i in range(10):
              value_pool.append(str(i))
    if special:
        value_pool.extend(string_to_chars("#$%&@^`~"))
    if extended:
        extended_ascii_characters = [chr(i) for i in range(128, 256)]
        value_pool.extend(string_to_chars(extended_ascii_characters))
    if punct:
        value_pool.extend(string_to_chars(".,:;"))
    if quotes:
        value_pool.extend(string_to_chars(""""'"""))
    if dashes:
        value_pool.extend(string_to_chars("\\/|_-"))
    if math:
        value_pool.extend(string_to_chars("<>*+!?="))
    if braces:
        value_pool.extend(string_to_chars("{[()]}"))
    if exclude:
        values_to_exclude.extend(list_string_to_chars(exclude))
        
    updated_value_pool = exclude_values(value_pool, values_to_exclude)
    for i in range(num_pass):
        click.echo(generate_password(length, updated_value_pool))

def string_to_chars(string_items):
    """
    Take in a string and split into a list of individual characters
    in a list and return that list

    Parameters:
    - string_items

    Returns:
    List
    """
    return [char for char in string_items]

def list_string_to_chars(list_string_items):
    """
    Take in a list that includes strings and tansform it into
    a new list of individual characters

    Parameters:
    - string_items

    Returns:
    List
    """
    return [char for word in list_string_items for char in word]

def exclude_values(value_pool, values_to_exclude):
    """
    Take in a list of values to filter and remove them from
    the value pool

    Parameters:
    - value_pool
    - values_to_exclude

    Returns:
    List
    """
    for i in values_to_exclude:
        value_pool.remove(i)
        
    return value_pool

def generate_password(length, value_pool):
    """
    Take in a value_pool list and randomly select values from
    it until the required length is met

    Parameters:
    - length
    - value_pool

    Returns:
    String
    """
    generated_password_list = random.choices(value_pool, k=length)
    generated_password_string = ''.join(generated_password_list)
    return generated_password_string

if __name__ == '__main__':
    cli()