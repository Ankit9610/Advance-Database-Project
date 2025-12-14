// Bulk insert TransactionLogs (use loop or array of 100 objects)
use('FinanceTracker');
db.transaction_logs.insertMany(Array.from({length: 100}, (_, i) => ({
    log_id: i+1,
    user_id: Math.floor(Math.random() * 100) + 1,
    category_id: Math.floor(Math.random() * 10) + 1,
    amount: Math.random() * 1000,
    date: new Date(),
    notes: `Note for log ${i+1}`,
    tags: ["tag1", "tag2"]
})));