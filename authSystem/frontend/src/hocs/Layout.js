import React from 'react';
import Navbar from '../containers/Navbar';
import { connect } from 'react-redux';
import { checkAuthenticated, load_user } from '../actions/auth';


const Layout = (props) => {
	
	useEffect(()=>{
		props.checkAuthenticated();
		props.load_user();
	},[]);
	
		return (
		<div>
			<Navbar />
			{props.children}
		</div>
		);
};

export default connect(null,{checkAuthenticated, load_user})(Layout);