import React, { Component } from 'react';
import Button from '@mui/material/Button';
import { link } from 'react-router-dom';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/Button';

export default class AnotherPage extends Component {
	constructor(props) {
		super(props);
	}
	
	render(){
		return (
			<Grid container spacing={1}>
				<Grid item xs={12} align="center">
					<Typography component="h4" variant="h4">
						Test typography
					</Typography>
					<Typography component="h4" variant="h4">
						Test typography
					</Typography>
					<Typography component="h4" variant="h4">
						Test typography
					</Typography>
				</Grid>
			</Grid>
		);
	}
}
