import React, { Component } from 'react';
import AnotherPage from "./AnotherPage";
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from 'react-router-dom';
import Button from '@mui/material/Button';
//Switch replaced with Routes in react-router-dom v6
//npm install @mui/material @mui/styled-engine-sc styled-components
//npm install @emotion/react 
//npm install @emotion/styled
export default class HomePage extends Component {
	constructor(props) {
		super(props);
	}
	
	render(){
		return (
			<Router>
				<Routes>
					<Route exact path='/' element={<h1>This is HomePage</h1>} />
					
					<Route path='/another' element={<AnotherPage/>} />
				</Routes>
			</Router>
		);
	}
}
