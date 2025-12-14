use('FinanceTracker');


// Update TransactionLogs
db.transaction_logs.updateOne({ log_id: 1 }, { $set: { notes: "Updated note" } });
db.transaction_logs.updateMany({ tags: "urgent" }, { $inc: { amount: 50 } });


// Update UserReviews
db.user_reviews.updateOne({ review_id: 1 }, { $set: { feedback: "Great category!" } });
