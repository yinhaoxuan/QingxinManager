import React from 'react'
import {Box, List, ListItem, ListItemIcon, ListItemText, Typography} from "@material-ui/core";
import PersonIcon from '@material-ui/icons/Person';
import DescriptionIcon from '@material-ui/icons/Description';
import BusinessIcon from '@material-ui/icons/Business';

const ListDisplay = (props) => {
    return (
        <Box>
            <Typography variant='subtitle1'>{props.Title}</Typography>
            <List>
                {props.List.map((row, index) => {
                    return (
                        <ListItem button component='a' href={'#/' + props.Type + '/' + row.id}>
                            <ListItemIcon>
                                {props.Type === 'person' ? <PersonIcon/> : props.Type === 'article' ?
                                    <DescriptionIcon/> : <BusinessIcon/>}
                            </ListItemIcon>
                            <ListItemText primary={row.name}/>
                        </ListItem>
                    )
                })}
            </List>
        </Box>
    )
}

export default ListDisplay