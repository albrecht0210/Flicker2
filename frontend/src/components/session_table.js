import { Button, IconButton, Paper, Stack, Table, TableBody, TableCell, TableContainer, TableFooter, TableHead, TableRow } from '@mui/material';
import { Component } from 'react';
import { EditRounded } from '@mui/icons-material';

class SessionTable extends Component {
    render() {
        const isEmpty = this.props.isEmpty;
        const sessions = this.props.sessions;
        const table_action = this.props.table_action;
        const handleOpen = this.props.handleOpen;

        return (
            <TableContainer component={Paper}>
                <Table aria-label="Session Table">
                    <TableHead>
                        <TableRow>
                            <TableCell>Action</TableCell>
                            <TableCell>Session</TableCell>
                            <TableCell>Type</TableCell>
                            <TableCell>Date & Time</TableCell>
                            <TableCell>Status</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody sx={{ height: 200 }}>
                    {isEmpty && 
                        <TableRow>
                            <TableCell>No data.</TableCell>
                        </TableRow>
                    }
                    {!isEmpty &&
                        sessions.map((session, index) => (
                            <TableRow key={index}>
                                <TableCell>
                                    <Stack direction="row" spacing={2}>
                                        <Button variant='contained' size='small' sx={{ backgroundColor: "#9C7B16" }}>{table_action.name}</Button>
                                        <IconButton aria-label="edit"><EditRounded/></IconButton>
                                    </Stack>
                                </TableCell>
                                <TableCell>{session.title}</TableCell>
                                <TableCell>{session.type}</TableCell>
                                <TableCell>{session.date_time}</TableCell>
                                <TableCell>{session.status}</TableCell>
                            </TableRow>
                        ))
                    }
                    </TableBody>
                    {table_action.name === "start" &&
                        <TableFooter>
                            <TableRow>
                                <TableCell>
                                    <Button onClick={handleOpen} variant='contained' size='small' sx={{ backgroundColor: "#9C7B16" }}>create</Button>
                                </TableCell>
                            </TableRow>
                        </TableFooter>
                    }
                </Table>
            </TableContainer>
        )
    }

}

export default SessionTable;