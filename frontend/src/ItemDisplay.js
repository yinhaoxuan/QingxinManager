import React, {Component} from 'react'
import {Chip} from "@material-ui/core";
import PersonIcon from "@material-ui/icons/Person";
import DescriptionIcon from "@material-ui/icons/Description";
import BusinessIcon from "@material-ui/icons/Business";

function to_icon(type) {
    return type === 'person' ? <PersonIcon/> : type === 'article' ?
        <DescriptionIcon/> : <BusinessIcon/>
}

const ItemDisplay = (props) => {
    return (
        <Chip clickable icon={to_icon(props.Type)} label={props.Data.name} component='a' href={'#/' + props.Type + '/' + props.Data.id}/>
    )
}

export default ItemDisplay