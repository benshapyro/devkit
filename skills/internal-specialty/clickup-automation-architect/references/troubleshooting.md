# Automation Troubleshooting Guide

Diagnose and fix common ClickUp automation problems.

## Accessing Automation Logs

1. Click "Automate" in sidebar
2. Click "Manage Automations"
3. Select "Activity" tab
4. Filter by: Location, Status (Success/Failed), Date range

**Business+ plans retain 180 days of automation history.**

## Common Issues and Solutions

### Automation Not Firing

**Symptom:** Trigger event occurs, but automation doesn't execute.

**Diagnostic steps:**

1. **Check if automation is enabled**
   - Manage Automations → Find automation → Verify toggle is ON
   - Automations auto-disable after 5 failures in one week

2. **Verify trigger event actually occurred**
   - Check task activity log for the expected change
   - Confirm the change was made by a user (not another automation in some cases)

3. **Review conditions**
   - Conditions may be too restrictive
   - Test by temporarily removing conditions one-by-one
   - Common issue: "Assignee is not empty" fails when task has no assignee

4. **Check scope**
   - List-level automation won't fire on tasks in other Lists
   - Space-level automation won't fire on tasks in other Spaces

5. **Verify monthly limit not exceeded**
   - Manage Automations → Usage tab
   - If at 100%, all automations paused until next month

6. **Check user permissions**
   - The automation creator must have permission to perform the action
   - Guest users cannot create automations that affect items they can't access

**Quick fixes:**
- Re-save the automation (sometimes triggers re-registration)
- Duplicate the automation, test duplicate, delete original if duplicate works
- Check for conflicting automations that might be changing the same fields

---

### Automation Fires Unexpectedly

**Symptom:** Automation triggers when it shouldn't.

**Diagnostic steps:**

1. **Review trigger scope**
   - Space-level triggers fire for ALL tasks in Space (including new Lists)
   - May need to add List condition to narrow scope

2. **Check for overlapping automations**
   - Multiple automations with similar triggers can cause confusion
   - Automation A might change something that triggers Automation B

3. **Examine condition logic**
   - Conditions use AND logic by default
   - "Status is Complete OR Priority is High" means EITHER triggers it

4. **Look for automation chains**
   - Automation A changes status → triggers Automation B → which triggers Automation C
   - Can cause unexpected cascades

**Quick fixes:**
- Add more specific conditions (List IS, Assignee IS, Tag CONTAINS)
- Move automation to narrower scope (Space → Folder → List)
- Add "Task type is NOT Subtask" condition if subtasks shouldn't trigger

---

### Automation Auto-Disabled

**Symptom:** Automation shows as disabled, didn't manually turn off.

**Cause:** ClickUp auto-disables after **5 failures in one week** with the same error.

**Resolution:**
1. Check Activity tab for error messages
2. Identify root cause (see Error Messages section below)
3. Fix the underlying issue
4. Re-enable the automation
5. Test with a real task

**Prevention:**
- Test automations thoroughly before deploying
- Monitor Activity tab weekly for failures
- Set up Slack/email notifications for automation failures (if available)

---

### Actions Not Completing

**Symptom:** Automation fires (shows in Activity) but action doesn't complete.

**Common causes:**

1. **Target doesn't exist**
   - "Move to List X" but List X was deleted or renamed
   - "Assign to [Person]" but person was removed from Workspace

2. **Permission issues**
   - Automation creator doesn't have permission to modify target
   - Guest-created automations have limited capabilities

3. **Field value conflicts**
   - Setting dropdown to value that doesn't exist
   - Setting date to invalid format

4. **Rate limiting**
   - Too many automations firing simultaneously
   - API rate limit (100/min Business) exceeded

**Quick fixes:**
- Verify all referenced items (Lists, users, field values) still exist
- Check that automation creator has appropriate permissions
- Add small delays between high-volume automations if possible

---

## Error Messages Reference

### "Value must be option index or uuid"

**Cause:** Dropdown or status field mapping issue.

**Details:** When automation tries to set a dropdown/status field, it's passing the display name instead of the internal ID.

**Solution:**
- Use ClickUp's built-in field selection (don't manually type values)
- If using Zapier/Make, use Formatter step to map names to IDs
- Re-create the action, selecting field value from dropdown

---

### "Task not found"

**Cause:** Referenced task was deleted, or task ID is incorrect.

**Common scenarios:**
- Automation references a specific task that was deleted
- Webhook payload contains outdated task ID
- Task was moved to a different List/Space the automation can't access

**Solution:**
- Update automation to reference correct task or use dynamic reference
- Add error handling in external integrations
- Verify task exists before automation runs (via conditions)

---

### "Insufficient permissions"

**Cause:** Automation creator lacks permission for the action.

**Common scenarios:**
- Member-level user creating automation that modifies admin-only fields
- Guest trying to create automation affecting non-shared items
- Automation trying to access Private Space the creator isn't in

**Solution:**
- Have Admin or Owner create/own the automation
- Verify automation creator has access to all referenced items
- Move automation ownership if original creator leaves

---

### "Rate limit exceeded"

**Cause:** Too many API calls in short period.

**Business tier limit:** 100 requests/minute
**Enterprise tier limit:** 10,000 requests/minute

**Solution:**
- Reduce automation frequency
- Add conditions to filter unnecessary triggers
- Batch operations where possible
- Upgrade to higher tier if consistently hitting limits

---

### "Webhook timeout"

**Cause:** External service didn't respond in time.

**Common scenarios:**
- External API is down or slow
- Network issues between ClickUp and external service
- External service requires authentication that expired

**Solution:**
- Test webhook endpoint directly (use Postman or curl)
- Verify external service is operational
- Check authentication credentials/tokens
- Implement retry logic in external service
- Add timeout handling

---

### "Loop detected"

**Cause:** Automation A triggers Automation B which triggers Automation A.

**Example:**
- Automation A: When status changes to "Review" → Add comment
- Automation B: When comment added → Change status to "Review"

**Solution:**
- Map out automation dependencies to identify loops
- Add conditions to break the cycle (e.g., "Only if comment is not from automation")
- Consolidate into single automation with multiple actions
- Use Custom Field flag to track if automation already ran

---

## Debugging Workflow

When automation behaves unexpectedly:

```
Step 1: Check Activity Log
  └─ Did automation fire? → If no, trigger/condition issue
  └─ Did it succeed? → If no, check error message
  └─ Did it fail? → See Error Messages section

Step 2: Reproduce Manually
  └─ Perform the trigger action manually on a test task
  └─ Watch Activity log in real-time
  └─ Note exact behavior vs expected

Step 3: Isolate Variables
  └─ Temporarily disable other automations
  └─ Remove conditions one-by-one
  └─ Test each action individually

Step 4: Check External Dependencies
  └─ Are all referenced items (Lists, users, fields) valid?
  └─ Are external services (webhooks) operational?
  └─ Are permissions correct for automation creator?

Step 5: Rebuild if Necessary
  └─ Sometimes easier to recreate than debug
  └─ Document the working configuration
  └─ Delete problematic automation, create fresh
```

## Preventive Measures

1. **Test before deploying**
   - Create test task and trigger automation
   - Verify all actions complete as expected
   - Check Activity log for any errors

2. **Document automations**
   - Maintain wiki/doc with all automations
   - Include: Name, Location, Trigger, Conditions, Actions, Owner, Date Created
   - Update when changes made

3. **Regular audits**
   - Monthly review of Activity logs
   - Identify and investigate recurring failures
   - Clean up unused automations

4. **Ownership management**
   - Assign automation owners
   - Transfer ownership when people leave
   - Avoid creating automations under guest accounts

5. **Version control**
   - Before changing automation, document current config
   - Test changes in staging List if possible
   - Rollback plan if changes cause issues
