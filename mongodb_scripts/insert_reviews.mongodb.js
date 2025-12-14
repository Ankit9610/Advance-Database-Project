use('FinanceTracker');


//  Bulk insert 100 user_reviews 
db.user_reviews.insertMany(Array.from({length: 100}, (_, i) => ({
    review_id: i+1,
    user_id: Math.floor(Math.random() * 100) + 1,
    category_id: Math.floor(Math.random() * 10) + 1,
    rating: Math.floor(Math.random() * 5) + 1,
    feedback: `Feedback for review ${i+1}: This category is ${['great', 'okay', 'poor'][Math.floor(Math.random() * 3)]}.`,
    date: new Date()
})));
