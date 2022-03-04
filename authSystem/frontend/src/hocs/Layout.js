import React from 'react';
import Navbar from '../containers/Navbar';
const Layout = (props) => (
		<div>
			<Navbar />
			{props.children}
		</div>
);

export default Layout;