document.addEventListener('DOMContentLoaded', function() {
  const signLanguage = document.getElementById('signLanguage');
  const outputMode = document.getElementById('outputMode');

  // Load saved settings
  chrome.storage.sync.get(['signLanguage', 'outputMode'], function(data) {
    signLanguage.value = data.signLanguage || 'asl';
    outputMode.value = data.outputMode || 'captions';
  });

  // Save settings on change
  signLanguage.addEventListener('change', function() {
    chrome.storage.sync.set({signLanguage: signLanguage.value});
  });

  outputMode.addEventListener('change', function() {
    chrome.storage.sync.set({outputMode: outputMode.value});
  });
});
