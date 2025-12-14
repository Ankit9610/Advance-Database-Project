use('FinanceTracker');


// Read TransactionLogs
db.transaction_logs.find({ amount: { $gt: 100 } }).sort({ date: -1 });

// Read UserReviews

db.user_reviews.find({ rating: { $gte: 4 } }, { feedback: 1 });

// Read BudgetPlans
db.budget_plans.find({});

// Aggregation: Average rating per category
db.user_reviews.aggregate([
    { $group: { _id: "$category_id", avgRating: { $avg: "$rating" } } }
]);










use('FinanceTracker');

// 1. Find all logs that have the tag "food" inside their array
// SQL makes this hard (requires complex joins/parsing), MongoDB does it in very easy way.
const foodLogs = db.transaction_logs.find({ tags: "food" });

// Just to check during video presentation. Alll spendimg on food etc....
 console.log("Found transactions tagged with 'food':");
 console.log(foodLogs);