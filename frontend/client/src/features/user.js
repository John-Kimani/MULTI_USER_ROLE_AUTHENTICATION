import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";


export const register = createAsyncThunk(
  "users/register",
  async ({ email, username, phone_number, password }, thunkAPI) => {
    const body = JSON.stringify({
      email,
      username,
      phone_number,
      password
    })

    try {
      const res = await fetch('api/users/register/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body:body,

      })

      const data = await res.json();

      if (res.status === 201){
        return data;
      }else {
        return thunkAPI.rejectWithValue(data);
      }
    }catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);


const getUser = createAsyncThunk('users/me/', async (_, thunkAPI) => {
  console.log('Start')
  try{

    const res = await fetch('api/users/me/', {
      method: "GET",
      headers: {
        Accept: 'application/json',
      }
    })

    const  data = await res.json();

    if(res.status == 200){
      return data;
    }else{
      return thunkAPI.rejectWithValue(data);
    }
  }catch(err){
    return thunkAPI.rejectWithValue(err.response.data);
  }
});


export const login = createAsyncThunk(
  "users/login",
  async ({ email, password }, thunkAPI) => {
    const body = JSON.stringify({
      email,
      password
    })

    try {
      const res = await fetch('api/users/login/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body,

      })

      const data = await res.json();

      if (res.status === 200){
        const { dispatch } = thunkAPI;



        dispatch(getUser());

        return data;
      }else {
        return thunkAPI.rejectWithValue(data);
      }
    }catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

const initialState = {
  isAuthenticated: false,
  user: null,
  loading: false,
  registered: false,
};

const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    resetRegistered: (state) => {
      // Sync action creators dispatch on the login page
      state.registered = false;
    },
    //Handles syncronous dispatches using the thunk middleware to generate action creators
  },
  extraReducers: builder => {
    builder
    .addCase(register.pending, state => {
      state.loading = true;
    })
    .addCase(register.fulfilled, state => {
      state.loading = false;
      state.registered = true;
    })
    .addCase(register.rejected, state => {
      state.loading = false;
    })
    .addCase(login.pending, state => {
      state.loading = true;
    })
    .addCase(login.fulfilled, state => {
      state.loading = false;
      state.isAuthenticated = true;
    })
    .addCase(login.rejected, state => {
      state.loading = false;
    })
    .addCase(getUser.pending, state => {
      state.loading = true;
    })
    .addCase(getUser.fulfilled, (state, action) => {
      state.loading = false;
      state.user = action.payload;
    })
    .addCase(getUser.rejected, state => {
      state.loading = false;
    })
  }
});

export const { resetRegistered } = userSlice.actions;
export default userSlice.reducer;
