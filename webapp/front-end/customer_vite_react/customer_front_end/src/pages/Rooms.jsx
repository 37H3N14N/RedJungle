import React from 'react'
import './Rooms.css'
import RoomTablet from '../components/RoomTablet'

const complete_room_data = [
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
    {
        'image_src':'http://redjungle-00.lab/images/shot_1.png',
        'price_tag':847.12,
        'room_name':'Pentium Cerritos',
        'description':"adventures of the support crew, specifically four junior officers, on the USS Cerritos, one of Starfleet's less important ships, in the late 24th century"
    },
]


function Rooms() {
  return (
    <div className='main_div' >
        {complete_room_data.map((singular_room_data)=> {
            return(
                <RoomTablet
                    image_src={singular_room_data['image_src']}
                    price_tag={singular_room_data['price_tag']}
                    room_name={singular_room_data['room_name']}
                    description={singular_room_data['description']}
                />
            )
        })}
    </div>
  )
}

export default Rooms