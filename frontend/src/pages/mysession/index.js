import { Box } from "@mui/material";
import { Component } from "react";
import SessionTable from "../../components/session_table";
import axios from "axios";
import SessionDialog from "./components/session_dialog";

class MySession extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mySessionsList: [],
            createDialogOpen: false 
        }
    }
    componentDidMount() {
        this.refreshTableData();
    }

    refreshTableData = async() => {
        await axios
            .get('http://localhost:8000/api/sessions/user/1/')
            .then((res) => this.setState({ mySessionsList: res.data }))
            .catch((err) => console.log(err));
    }

    handleCreateDialogClose = () => {
        this.setState({createDialogOpen: false})
    }

    handleCreateDialogOpen = () => {
        this.setState({createDialogOpen: true})
    }

    render() {
        return (
            <Box sx={{ padding: 3.5 }}>
                <SessionTable 
                    isEmpty={this.state.mySessionsList.length === 0} 
                    sessions={this.state.mySessionsList} 
                    table_action={{name: "start"}}
                    handleOpen={this.handleCreateDialogOpen}
                />
                <SessionDialog
                    open={this.state.createDialogOpen}
                    handleClose={this.handleCreateDialogClose}
                    title="CREATE"
                />
            </Box>
        )
    }
}

export default MySession;