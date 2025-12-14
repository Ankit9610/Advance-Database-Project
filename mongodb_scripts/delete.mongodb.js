use('FinanceTracker');
// Delete from TransactionLogs
db.transaction_logs.deleteOne({ log_id: 1 });
db.transaction_logs.deleteMany({ amount: { $lt: 100 } });
db.transaction_logs.deleteMany({});

// Delete from UserReviews
db.user_reviews.deleteOne({ review_id: 1 });
db.user_reviews.deleteMany({ rating: { $lt: 3 } });

// Delete from BudgetPlans
db.budget_plans.deleteOne({ plan_id: 1 });
db.budget_plans.deleteMany({ user_id: 1 });
