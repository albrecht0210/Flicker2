import { Divider, Drawer, List, ListItem, ListItemButton, ListItemText, Toolbar } from "@mui/material";
import { Component } from "react";

class Sidebar extends Component {
    render() {
        const drawerWidth = this.props.drawerWidth;

        return (
            <Drawer 
                sx={{
                    width: drawerWidth,
                    flexShrink: 0,
                    '& .MuiDrawer-paper': {
                        width: drawerWidth,
                        boxSizing: 'border-box',
                    },
                }}
                variant="permanent"
                anchor="left"
            >
                <Toolbar />
                <Divider />
                <List>
                    {['All Sessions', 'My Sessions', 'History'].map((item, index) => (
                        <ListItem key={index}>
                            <ListItemButton>
                                <ListItemText primary={item} />
                            </ListItemButton>
                        </ListItem>
                    ))}
                </List>
                <Divider />
                <List>
                    {['Account', 'Logout'].map((item, index) => (
                        <ListItem key={index}>
                            <ListItemButton>
                                <ListItemText primary={item} />
                            </ListItemButton>
                        </ListItem>
                    ))}
                </List>
            </Drawer>
        )
    }
}

export default Sidebar;