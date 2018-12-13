"""
Module containing navegation menus
"""

def menu_start():
	prompt = 'Slab minimum steel reinforcement calculator\nPlease chose an option:\n'
	prompt += '<N>ew project, <L>oad project, e<X>it: '
	available = ['n', 'N', 'l', 'L', 'x', 'X'] 
	action = input(prompt)
	while action not in available:
		prompt = 'That option is not available here. Please chose one of the available options.\n'
		prompt = 'Slab minimum steel reinforcement calculator\nPlease chose an option:\n'
		prompt += '<N>ew project, <L>oad project, e<X>it: '
		action = input(prompt)
	return action

	
def menu_new_project():
	prompt = 'New project\nPlease chose an option:\n'
	prompt += '<N>ame, N<u>mber, <D>ate, <B>ack, e<X>it: '
	available = ['n', 'N', 'u', 'U', 'd', 'D', 'b', 'B', 'x', 'X'] 
		while action not in available:
		prompt = 'That option is not available here. Please chose one of the available options.\n'
		prompt = 'Slab minimum steel reinforcement calculator\nPlease chose an option:\n'
		prompt += '<N>ew project, <L>oad project, e<X>it: '
		action = input(prompt)
	return action
	

def menu_new_floor():
	prompt = 'New floor\nPlease chose an option:\n'
	prompt += '<N>ame, <E>levation , e<X>it: '
	return input(prompt)
	
	
def menu_new_slab():
	prompt = 'New slab\nPlease chose an option:\n'
	prompt += '<N>ame, <T>hickness, <C>oncrete strength, e<X>it: '
	return input(prompt)


def menu_concrete_strength():
	prompt = "Concrete strength\nInput the value of f'c in MPa: "
	return input(prompt)
	
	
def menu_new_engineer():
	prompt = 'New engineer\nPlease chose an option:\n'
	prompt += '<N>ame, <T>itle, <O>IQ number, e<X>it: '
	return input(prompt)
	
	
def menu_new_band():
	prompt = 'Create new strip\n'
	prompt += '<C>olumn, <M>id, e<X>it: '
	input(prompt)

	
def menu_column_band():
	prompt = ''
	prompt += ''
	input(prompt)
