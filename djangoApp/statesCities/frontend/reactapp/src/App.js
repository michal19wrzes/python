import React, { Component } from 'react';
import {BrowserRouter as Router, Routes, Route,} from 'react-router-dom';



export default class App extends Component {
	constructor(props) {
		super(props);
	}
	
	render(){
		return (
			<Router>
				<Routes>
					<Route exact path='/login' element={<h1>TO JEST LOGIN</h1>} />
				</Routes>
			</Router>
		);
	}
}