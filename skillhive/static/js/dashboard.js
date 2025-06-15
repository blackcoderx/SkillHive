 const tabBtns = document.querySelectorAll('.tab-btn');
  const skillsTab = document.getElementById('skills-tab');
  const requestsTab = document.getElementById('requests-tab');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      if (btn.dataset.tab === 'skills') {
        skillsTab.style.display = '';
        requestsTab.style.display = 'none';
      } else {
        skillsTab.style.display = 'none';
        requestsTab.style.display = '';
      }
    });
  });


// pop over functionality
document.querySelector('.skills-header button').addEventListener('click', function() {
  document.getElementById('addSkillPopover').style.display = 'flex';
});
// Hide popover
document.getElementById('closePopoverBtn').addEventListener('click', function() {
  document.getElementById('addSkillPopover').style.display = 'none';
});
