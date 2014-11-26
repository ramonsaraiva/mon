import sdl2
import sdl2.ext

keyboard = {'moving_ws': 0,
			'moving_da': 0,
			'looking': 0}

mouse = {'y': 0, 'x': 0}

def keyboard_moving(orientation, direction):
	keyboard['moving_{0}'.format(orientation)] = direction

def keyboard_moving_stop(orientation):
	keyboard['moving_{0}'.format(orientation)] = 0

def keyboard_status():
	return keyboard

def mouse_status():
	m = dict(mouse)
	mouse['x'] = mouse['y'] = 0
	return m

def keyboard_down(event):
	sym = event.keysym.sym

	if sym is sdl2.SDLK_q:
		exit()
	
	if sym is sdl2.SDLK_w:
		keyboard_moving('ws', 1)
		return

	if sym is sdl2.SDLK_s:
		keyboard_moving('ws', -1)
		return

	if sym is sdl2.SDLK_d:
		keyboard_moving('da', -1)
		return

	if sym is sdl2.SDLK_a:
		keyboard_moving('da', 1)
		return

def keyboard_up(event):
	sym = event.keysym.sym

	if sym is sdl2.SDLK_w or sym is sdl2.SDLK_s:
		keyboard_moving_stop('ws')
		return
	if sym is sdl2.SDLK_d or sym is sdl2.SDLK_a:
		keyboard_moving_stop('da')

def mouse_down(event):
	button = event.button
	if button is sdl2.SDL_BUTTON_RIGHT:
		keyboard['looking'] = 1

def mouse_up(event):
	button = event.button
	if button is sdl2.SDL_BUTTON_RIGHT:
		keyboard['looking'] = 0

def mouse_motion(event):
	if not keyboard['looking']:
		return
	mouse['x'] = 0.35 * event.xrel
	mouse['y'] = -0.01 * event.yrel

def check():
	events = sdl2.ext.get_events()
	for event in events:
		if event.type == sdl2.SDL_KEYDOWN:
			keyboard_down(event.key)
			continue
		if event.type == sdl2.SDL_KEYUP:
			keyboard_up(event.key)
			continue
		if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
			mouse_down(event.button)
			continue
		if event.type == sdl2.SDL_MOUSEBUTTONUP:
			mouse_up(event.button)
			continue
		if event.type == sdl2.SDL_MOUSEMOTION:
			mouse_motion(event.motion)

	# 60 fps?
	sdl2.SDL_Delay(10)
