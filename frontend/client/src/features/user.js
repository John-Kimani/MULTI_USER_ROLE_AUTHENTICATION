import { createSlice } from '@reduxjs/toolkit'

const initialState = { 
    isAuthenticated: false,
    user: null,
    loading: false,
    registered: false,
}



const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    resetRegistered: state => {
      // Sync action creators dispatch on the login page
      state.registered = false;
    }
    //Handles syncronous dispatches using the thunk middleware to generate action creators
  },
})

export const { resetRegistered } = userSlice.actions
export default userSlice.reducer