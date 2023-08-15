"""
Leetcode 86: Partition List https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes
less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

Constraints:
    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200
"""


from typing import Optional


class ListNode:
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
	if head == None:
		return None  # Exit early, no work to do
	lt_x = []
	geq_x = []
	traversal_node = head
	# Looping forward through list preserves order
	while (not(traversal_node == None)):  # While there is a next node
		if (traversal_node.val < x):  # If less than x
			lt_x.append(traversal_node.val)  # Add to lt_x list
		else:
			geq_x.append(traversal_node.val)  # Add to geq_x list
		traversal_node = traversal_node.next  # Go to the next node

	if (len(geq_x) > 0):  # Check if there are any elements >= x
		# Build the list backwards from the last element of geq_x
		geq_node = ListNode(geq_x[-1], None)  # Tail of list
		for i in range(len(geq_x) - 2, -1, -1):
			temp = geq_node  # Save previously generated node
			# Make a new node with temp as next
			geq_node = ListNode(geq_x[i], temp)
		
		if (len(lt_x) == 0):
			return geq_node  # If lt_x is empty, then geq_node is head

	# If we did not return, then there are elements in lt_x to process

	# Build the last lt_node with next set to the last geq_node
	if (len(geq_x) > 0):
		lt_node = ListNode(lt_x[-1], geq_node)
	else:
		lt_node = ListNode(lt_x[-1], None)  # Or as tail if geq_x is empty
	
	# Build the rest of the list backwards from the last lt_node
	for i in range(len(lt_x) - 2, -1, -1): 
		temp = lt_node  # Save previously generated node
		# Make a new node with temp as next
		lt_node = ListNode(lt_x[i], temp)
	return lt_node  # Now contains head

# Test cases
def parse_list(head: Optional[ListNode]) -> str:
	output = "["
	traversal_node = head
	while (not(traversal_node == None)):
		output += str(traversal_node.val) + " -> "
		traversal_node = traversal_node.next
	return output + "None]"

def test_case_setup(test_case: int) -> Optional[ListNode]:
	match test_case:
		case 1:
			# Test case 1 setup #
			node_5 = ListNode(2)
			node_4 = ListNode(5, node_5)
			node_3 = ListNode(2, node_4)
			node_2 = ListNode(3, node_3)
			node_1 = ListNode(4, node_2)
			head = ListNode(1, node_1)
			# End test case 1 setup #
		case 2:
			# Test case 2 setup #
			node_1 = ListNode(1)
			head = ListNode(2, node_1)
			# End test case 2 setup #
		case 3:
			# Test case 3 setup #
			head = None
			# End test case 3 setup #
		case 4:
			# Test case 4 setup #
			head = ListNode(1)
			# End test case 4 setup #
		case 5:
			# Test case 5 setup #
			head = ListNode(1)
			# End test case 5 setup #
	return head

testCaseXs = [3, 2, 0, 0, 2]
testCaseExpectedStrings = ["[1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None]",
			   									 "[1 -> 2 -> None]",
													 "[None]",
													 "[1 -> None]",
													 "[1 -> None]"]

print()
print("Testing Report")
print("-" * 60)
num_passed = 0
for i in range(len(testCaseXs)):
	head = test_case_setup(i + 1)
	output = partition(head, testCaseXs[i])
	print("partition(head,", str(testCaseXs[i]) + "): ", end = "")
	parsed_output = parse_list(output)
	print(parsed_output)
	print("          Expected:", testCaseExpectedStrings[i])
	if (parsed_output == testCaseExpectedStrings[i]):
		print("Test case", i + 1, "passed!")
		num_passed += 1
	else:
		print("Test case", i + 1, "failed!")
	print()

print("Test cases passed:", str(num_passed / len(testCaseXs) * 100) + "%")
print("-" * 60)