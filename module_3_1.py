calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(a):
    count_calls()
    a = {len(a), a.upper(), a.lower()}
    return a
def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search = [s.upper() for s in list_to_search]
    if string in list_to_search:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Megalodon'))
print(is_contains('Cinema', ['nema', 'CiNEmA', 'CiNE']))
print(is_contains('hand', ['hands', 'handfull]']))
print(calls)
