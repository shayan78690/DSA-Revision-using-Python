class Solution {
    class Node implements Comparable<Node> {
        int data;
        int row;
        int col;

        Node(int data, int row, int col) {
            this.data = data;
            this.row = row;
            this.col = col;
        }

        public int compareTo(Node node) {
            return this.data - node.data;
        }
    }

    public int[] smallestRange(List<List<Integer>> nums) {
        int n = nums.size();
        int mini = Integer.MAX_VALUE;
        int maxi = Integer.MIN_VALUE;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            int element = nums.get(i).get(0);
            mini = Math.min(mini, element);
            maxi = Math.max(maxi, element);
            pq.add(new Node(element, i, 0));
        }

        int start = mini;
        int end = maxi;
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            mini = node.data;
            if (maxi - mini < end - start) {
                start = mini;
                end = maxi;
            }

            if (node.col + 1 < nums.get(node.row).size()) {
                maxi = Math.max(maxi, nums.get(node.row).get(node.col + 1));
                pq.add(new Node(nums.get(node.row).get(node.col + 1), node.row, node.col + 1));
            } else {
                break;
            }
        }
        int ans[] = new int[2];
        ans[0] = start;
        ans[1] = end;
        return ans;
    }
}
