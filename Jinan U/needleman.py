# Implement the Needleman & Wensch Algorithm for global assignment

class GlobalAssign:
    def __init__(self, seq1, seq2, d=-5, match=2, mismatch=-5, trans=-7):
        self.seq1 = str(seq1)
        self.seq2 = str(seq2)
        self.mismatch = mismatch
        self.d = d
        self.trans = trans
        self.match = match

    def score(self, a, b):
        # score for any pair of bases
        pair = (str(a).capitalize(), str(b).capitalize())
        if pair in {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}:
            return self.mismatch
        if pair in {('A', 'C'), ('C', 'A'), ('T', 'G'), ('G', 'T'),
                    ('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')}:
            return self.trans
        if str(a).capitalize() == str(b).capitalize():
            return self.match

        elif a == '-' or b == '-':
            return self.d

    def score_matrix(self):
        """Using Nested Lists
        Transfer Direction:
            0: from diagnosis
            1: from left
            2: from up

        return a tuple of score_mat and trace_mat
        """
        score_mat = {}
        trace_mat = {}
        new_seq1 = '-' + self.seq1
        new_seq2 = '-' + self.seq2

        for i, p in enumerate(new_seq1):
            score_mat[i] = {}
            trace_mat[i] = {}
            for j, q in enumerate(new_seq2):
                if i == 0:  # gap in seq1
                    score_mat[i][j] = j*self.d
                    trace_mat[i][j] = 1
                    continue
                if j == 0:
                    score_mat[i][j] = i*self.d
                    trace_mat[i][j] = 2
                    continue
                # Write three score function
                formul = [score_mat[i-1][j-1] + self.score(p, q),  # diagnosis
                          score_mat[i][j-1] + self.score('-', q),  # from left
                          score_mat[i-1][j] + self.score(p, '-')]  # from up
                picked = max(formul)
                score_mat[i][j] = picked
                trace_mat[i][j] = formul.index(picked)
        return score_mat, trace_mat

    def print_matrix(self, seq1=None, seq2=None, m=None):
        """print score matrix or trace matrix"""
        if not seq1:
            seq1 = '-' + self.seq1
        if not seq2:
            seq2 = '-' + self.seq2
        if not m:
            print("Please score the matrix before print.")
        print('--------------------------------')
        print(' '.join(['%3s' % i for i in ' '+seq2]))
        for i, p in enumerate(seq1):
            line = [p] + [m[i][j] for j in range(len(seq2))]
            print(' '.join(['%3s' % i for i in line]))
        print('--------------------------------')
        return

    def traceback(self):
        '''
        find one optimal traceback path from trace matrix, return path code
        -!- CAUTIOUS: if multiple equally possible path exits, only return one of them -!-
        '''
        seq1, seq2 = '-' + self.seq1, '-' + self.seq2
        _,trace_mat = self.score_matrix()
        i, j = len(seq1) - 1, len(seq2) - 1
        path_code = ''
        while i > 0 or j > 0:
            direction = trace_mat[i][j]
            if direction == 0:                    # from up-left direction
                i = i-1
                j = j-1
                path_code = '0' + path_code
            elif direction == 1:                  # from left
                j = j-1
                path_code = '1' + path_code
            elif direction == 2:                  # from up
                i = i-1
                path_code = '2' + path_code
        return path_code

    def pretty_print_align(self,path_code=None):
        '''
        return pair alignment result string from
        path code: 0 for match, 1 for gap in seq1, 2 for gap in seq2
        '''
        align1 = ''
        middle = ''
        align2 = ''
        seq1,seq2 = self.seq1,self.seq2
        if not path_code:
            path_code = self.traceback()
        for p in path_code:
            if p == '0':
                align1 = align1 + seq1[0]
                align2 = align2 + seq2[0]
                if seq1[0] == seq2[0]:
                    middle = middle + '|'
                else:
                    middle = middle + ' '
                seq1 = seq1[1:]
                seq2 = seq2[1:]
            elif p == '1':
                align1 = align1 + '-'
                align2 = align2 + seq2[0]
                middle = middle + ' '
                seq2 = seq2[1:]
            elif p == '2':
                align1 = align1 + seq1[0]
                align2 = align2 + '-'
                middle = middle + ' '
                seq1 = seq1[1:]

        print('Alignment:\n\n   ' + align1 + '\n   ' + middle + '\n   ' + align2 + '\n')
        return
