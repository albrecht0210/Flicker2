import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, Stack, TextField } from "@mui/material";
import { Component } from "react";

class SessionDialog extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: "",
            type: -1,
            date: "",
            time: "",
            password: "",
            team: [],
            criteria: 0,
            host: 1
        }
    }
    render() {
        const open = this.props.open;
        const handleClose = this.props.handleClose;
        const title = this.props.title;

        return (
            <Dialog
                open={open}
                onClose={handleClose}
                aria-describedby="session-dialog"
            >
                <DialogTitle>
                    {title} SESSION
                </DialogTitle>
                <DialogContent>
                    <Grid container>
                        <Grid sm={6} xs={12} paddingRight={2}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="title"
                                label="Session TItle"
                                type="text"
                                fullWidth
                                variant="outlined"
                            />
                        </Grid>
                        <Grid sm={6} xs={12} paddingLeft={2}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                fullWidth
                                variant="outlined"
                            />
                        </Grid>
                        <Grid sm={6} xs={12} paddingRight={2}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                fullWidth
                                variant="outlined"
                            />
                        </Grid>
                        <Grid sm={6} xs={12} paddingLeft={2}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                fullWidth
                                variant="outlined"
                            />
                        </Grid>
                        <Grid sm={6} xs={12} paddingRight={2}>
                            <Stack spacing={1}>
                                <Button variant="contained" sx={{marginTop: 1}}>Import Team</Button>
                                <Button variant="contained">Select Criteria</Button>
                            </Stack>
                        </Grid>
                        <Grid sm={6} xs={12} paddingLeft={2}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                fullWidth
                                variant="outlined"
                            />
                        </Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose}>{title}</Button>
                    <Button onClick={handleClose}>Cancel</Button>
                </DialogActions>
            </Dialog>
        )
    }
}

export default SessionDialog;