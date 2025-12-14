use('FinanceTracker');


//  Bulk insert 100 budget_plans
db.budget_plans.insertMany(Array.from({length: 100}, (_, i) => ({
    plan_id: i+1,
    user_id: Math.floor(Math.random() * 100) + 1,
    goals: [
        { goal_name: `Goal 1 for plan ${i+1}`, target_amount: Math.random() * 10000, milestones: [`Milestone 1`, `Milestone 2`] },
        { goal_name: `Goal 2 for plan ${i+1}`, target_amount: Math.random() * 5000, milestones: [`Milestone A`, `Milestone B`] }
    ],
    notes: `Notes for budget plan ${i+1}: Aim to save more this year.`
})));
