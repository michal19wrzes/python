import {
	LOGIN_SUCCESS,
	LOGIN_FAIL,
	LOAD_USER_SUCCESS,
	LOAD_USER_FAIL,
	AUTHENTICATED_SUCCESS,
	AUTHENTICATED_FAIL,
	LOGOUT,
	RESET_PASSWORD_SUCCESS,
	RESET_PASSWORD_FAIL,
	USER_CREATE_SUCCESS,
	USER_CREATE_FAIL,
	RESET_PASSWORD_CONFIRM_FAIL,
	RESET_PASSWORD_CONFIRM_SUCCESS
} from '../actions/types';

const initialState = {
	access: localStorage.getItem('access'),
	refresh: localStorage.getItem('refresh'),
	isAuthenticated: null,
	user: null
};

export default function(state= initialState,action){
	const { type, payload } = action;
	
	switch(type) {
		case LOGIN_SUCCESS:
			localStorage.setItem('access', payload.access);
			return {
				...state,
				isAuthenticated: true,
				access: payload.access,
				refresh: payload.refresh
			}
		case LOGIN_FAIL:
		case LOGOUT:
			localStorage.removeItem('access');
			localStorage.removeItem('refresh');
			return {
				...state,
				isAuthenticated: false,
				access: null,
				refresh: null,
				user: null
			}
		case AUTHENTICATED_SUCCESS:
			return {
				...state,
				isAuthenticated: true
			}
		case AUTHENTICATED_FAIL:
			return {
				...state,
				isAuthenticated: false				
			}
		case LOAD_USER_SUCCESS:
			return {
				...state,
				user: payload
			}
		case LOAD_USER_FAIL:
			return {
				...state,
				user: null
			}
		case USER_CREATE_FAIL:
		case USER_CREATE_SUCCESS:
		case RESET_PASSWORD_SUCCESS:
		case RESET_PASSWORD_FAIL:
		case RESET_PASSWORD_CONFIRM_SUCCESS:
		case RESET_PASSWORD_CONFIRM_FAIL:
			return {
				...state
			}
		default:
			return state
	}
	
};