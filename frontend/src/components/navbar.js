import { AppBar, Toolbar, Typography } from '@mui/material';
import { Component } from 'react';

class Navbar extends Component {
    // constructor(props) {
    //     super(props);
    // }

    // componentDidMount() {
        
    // }

    render() {
        const drawerWidth = this.props.drawerWidth;

        return (
            <AppBar 
                position="fixed"
                sx={{width: `calc(100% - ${drawerWidth}px)`, ml: `${drawerWidth}px`, backgroundColor: 'white', color: 'black'}}
            >
                <Toolbar>
                    <Typography variant="h6" noWrap component="div">
                        Flicker
                    </Typography>
                </Toolbar>
            </AppBar>
        )
    }

}

export default Navbar;