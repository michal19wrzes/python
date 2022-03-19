import React, { useState } from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { connect } from 'react-redux';
import { Navigate } from 'react-router-dom';
import { activate_account } from '../actions/auth';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.success" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://github.com/michal19wrzes/python">
        M.N.
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const theme = createTheme();
 
const Activate = ({activate_account}) => {
	const [verified, setVerified] = useState(false);
	
	const handleSubmit = e => {
		const uid = match.params.uid;
		const token = match.params.token;
		activate_account(uid,token);
		setVerified(true);
	};
	
	if(verified){
		return <Navigate to='/' />
	}
  
	

	return (
	<ThemeProvider theme={theme}>
		  <Grid container component="main" sx={{ height: '100vh' }}>
			<CssBaseline />
			<Grid
			  item
			  xs={false}
			  sm={4}
			  md={7}
			  sx={{
				backgroundImage: 'url(https://source.unsplash.com/random)',
				backgroundRepeat: 'no-repeat',
				backgroundColor: (t) =>
				  t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
				backgroundSize: 'cover',
				backgroundPosition: 'center',
			  }}
			/>
			<Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
			  <Box
				sx={{
				  my: 8,
				  mx: 4,
				  display: 'flex',
				  flexDirection: 'column',
				  alignItems: 'center',
				}}
			  >
				<Avatar sx={{ m: 1, bgcolor: 'success.main' }}>
				  <LockOutlinedIcon />
				</Avatar>
				<Typography component="h1" variant="h5">
				  Aktywuj konto
				</Typography>
				<Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 1 }}>
				  
				  <Button
					type="submit"
					fullWidth
					color="success"
					variant="contained"
					sx={{ mt: 3, mb: 2 }}
				  >
					Aktywuj
				  </Button>
				  
				  <Copyright sx={{ mt: 5 }} />
				</Box>
			  </Box>
			</Grid>
		  </Grid>
		</ThemeProvider>
	);
};

export default connect(null,{ activate_account })(Activate);