class Solution:
    def sortStack(self, st):
        if not st:
            return st
        top = st.pop()
        self.sortStack(st)
        self.insert(st, top)
        
        return st
    
    def insert(self, st, element):
        if not st or st[-1] <= element:
            st.append(element)
            return
        top = st.pop()
        self.insert(st, element)
        st.append(top)
      
