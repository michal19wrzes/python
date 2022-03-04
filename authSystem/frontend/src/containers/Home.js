import React from 'react';
import Navbar from './Navbar';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import FormHelperText from '@mui/material/FormHelperText';
import FormControl from '@mui/material/FormControl';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormLabel from '@mui/material/FormLabel';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/Button';
import Stack from '@mui/material/Stack';


const Home = (props) => (
		<div>
			<Stack spacing ={2} align = 'center'>
				<Navbar />
				<h1>home</h1>
				<Typography component="h4" variant="h4">
					essa
					
				</Typography>
				<Button color="secondary" variant="contained" to="/" component={Link}>
					Back
				  </Button>
			</Stack>
		</div>
);

export default Home;