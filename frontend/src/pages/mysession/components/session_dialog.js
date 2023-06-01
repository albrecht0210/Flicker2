import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, Stack, TextField } from "@mui/material";
import { Component } from "react";

class SessionDialog extends Component {
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
                        <Grid sm={6} xs={12} paddingRight={4}>
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
                        <Grid sm={6} xs={12}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                variant="standard"
                            />
                        </Grid>
                        <Grid sm={6} xs={12}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                variant="standard"
                            />
                        </Grid>
                        <Grid sm={6} xs={12}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                variant="standard"
                            />
                        </Grid>
                        <Grid sm={6} xs={12}>
                            <Stack direction="row" spacing={2}>
                                <Button fullWidth>Import Team</Button>
                                <Button fullWidth>Select Criteria</Button>
                            </Stack>
                        </Grid>
                        <Grid sm={6} xs={12}>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="name"
                                label="Email Address"
                                type="email"
                                variant="standard"
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