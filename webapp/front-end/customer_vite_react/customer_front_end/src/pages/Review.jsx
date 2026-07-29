import React from 'react'
import './Review.css'
import ReviewTablet from '../components/ReviewTablet'

const complete_review_data = [
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
],
  [
    {
    'star_rating':'4.1',
    'review_message':'He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.He looked around, surrounded by his friend as they enjoyed the view.Today was a good day, he could feel it. The day he’d been waiting for, pushing for. He’d just have to wiggle a bit more and it would be his turn,his turn to explore the beautiful world that had laid before him since he was born.',
    'profile_picture':'../images/shot_1.png',
    'user_name':'Patric Star',
    'date':'12thMonthYear'
  }
]
]

function Review() {
  return (
    <div className='main_div_review'>
      {complete_review_data.map((singular_review_tablet) => {
        return(
          <ReviewTablet
          review_data = {singular_review_tablet}
          />
        )
      })}
    </div>
  )
}

export default Review