import React, { Component } from 'react';
import { render } from "react-dom";
import Home from './containers/Home';
import Signup from './containers/Signup';
import ResetPassword from './containers/ResetPassword';
import Login from './containers/Login';
import Activate from './containers/Activate';
import Navbar from './containers/Navbar';
import {BrowserRouter as Router, Routes, Route,} from 'react-router-dom';

export default class App extends Component {
	constructor(props) {
		super(props);
	}
	
	render(){
		return (
			<Router>
				
				<Routes>
					<Route exact path='/' element={<Home />} />
					<Route exact path='/signup' element={<Signup />} />
					<Route exact path='/reset-password' element={<ResetPassword />} />
					<Route exact path='/login' element={<Login />} />
					<Route exact path='/activate' element={<Activate />} />
					
					<Route path='/another' element={<h1>This is another</h1>} />
				</Routes>
				
			</Router>
		);
	}
}
/*get element by id*/