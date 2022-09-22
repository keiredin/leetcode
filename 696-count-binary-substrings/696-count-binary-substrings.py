class Solution(object):
    def countBinarySubstrings(self, S):
        n = len(S)
        # To store the total count
        # of substrings
        ans = 0;

        i = 0;

        # Traversing the string
        while (i < n) :

            # Count of consecutive
            # 0's & 1's
            cnt0 = 0; cnt1 = 0;

            # Counting subarrays of
            # type "01"
            if (S[i] == '0') :

                # Count the consecutive
                # 0's
                while (i < n and S[i] == '0') :
                    cnt0 += 1;
                    i += 1;

                # If consecutive 0's
                # ends then check for
                # consecutive 1's
                j = i;

                # Counting consecutive 1's
                while (j < n and S[j] == '1') :
                    cnt1 += 1;
                    j += 1;

            # Counting subarrays of
            # type "10"
            else :

                # Count consecutive 1's
                while (i < n and S[i] == '1') :
                    cnt1 += 1;
                    i += 1;

                # If consecutive 1's
                # ends then check for
                # consecutive 0's
                j = i;

                # Count consecutive 0's
                while (j < n and S[j] == '0') :
                    cnt0 += 1;
                    j += 1;

            # Update the total count
            # of substrings with
            # minimum of (cnt0, cnt1)
            ans += min(cnt0, cnt1);

        # Return answer
        return ans;
                    