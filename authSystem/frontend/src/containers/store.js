import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import auth from '../reducers/auth';

const initialState = {};

const middleware = [thunk];

const store = createStore(
	auth,
	initialState,
	composeWithDevTools(applyMiddleware(...middleware))
);

export default store;