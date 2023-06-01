import { Component } from "react"
import Sidebar from "../components/sidebar";
import { Box, Toolbar } from "@mui/material";
import Navbar from "../components/navbar";
import MySession from "./mysession";

class PageTemplate extends Component {
    render() {
        return (
            <Box sx={{ display: 'flex' }}>
                <Navbar drawerWidth={240} />
                <Sidebar drawerWidth={240} />
                <Box
                    component="main"
                    sx={{ flexGrow: 1, bgcolor: 'background.default', p: 3 }}
                >
                    <Toolbar />
                    <MySession />
                </Box>
            </Box> 
        )
    }
}

export default PageTemplate;