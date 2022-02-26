import React, { useState,Component } from 'react';
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


export default class AnotherPage extends Component {

  constructor(props) {
    super(props);
	this.state={
		value : "Falsz"
	};  
  }
  
  onChange = e =>{
	  this.setState({value : e.target.value});
  }
  
  render() {
	const{value} =this.state;
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            Create A Room
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <FormHelperText>
              <div align="center">Guest Control of Playback State</div>
            </FormHelperText>
            <RadioGroup>
              <FormControlLabel
                value="Prawda"
                control={<Radio color="primary" />}
				checked={value==="Prawda"}
				onChange={this.onChange}
                label="Play/Pause"
                labelPlacement="bottom"
              />
              <FormControlLabel
                value="Falsz"
                control={<Radio color="secondary" />}
				checked={value==="Falsz"}
				onChange={this.onChange}
                label="No Control"
                labelPlacement="bottom"
              />
            </RadioGroup>
          </FormControl>
        </Grid>
        
        <Grid item xs={12} align="center">
          <Button color="secondary" variant="contained" to="/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}
	