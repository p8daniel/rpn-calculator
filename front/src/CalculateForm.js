import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import axios from 'axios';

const MaterialUIForm = () => {
  const [inputValue, setInputValue] = useState('');
  const [displayValue, setDisplayValue] = useState('');
  const [error, setError] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();


    axios({
        method: "POST",
        url: `${process.env.REACT_APP_API_URL}/v0/rpnCalculate`,
        data: {
          expression: inputValue
        }
      })
      .then((response) => {
        console.log(response);
        setDisplayValue(response.data.data);
        setError(null);
      })
      .catch((error) => {
        console.error(error);
        setError(error.message);
        setDisplayValue(error.message);
      });

    
  };

  return (
    <Box maxWidth={400} m="auto">
      <form onSubmit={handleSubmit}>
        <Typography variant="h5" gutterBottom>
          Calculate from rpn notation string
        </Typography>
        <TextField
          label="Input rpn expression"
          variant="outlined"
          fullWidth
          margin="normal"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <Button type="submit" variant="contained" color="primary">
          Calculate
        </Button>
      </form>
      {displayValue && (
        <Box mt={3}>
          <Typography variant="h6">Result:</Typography>
          <Typography>{displayValue}</Typography>
        </Box>
      )}
    </Box>
  );
};


export default MaterialUIForm;
