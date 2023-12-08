var tiles = [];
var dialog, dialogOverlay, dialogCloseButton, dialogOkButton;
var triggeringElement;

window.addEventListener("DOMContentLoaded", function (e) {
  dialog = document.querySelector(".dialog");
  dialogOverlay = dialog.querySelector(".overlay");
  dialogCloseButton = dialogOverlay.querySelector(".close-button");
  dialogOkButton = dialogOverlay.querySelector(".ok-button");

  /**
    Once Slick has initialized, retrieve the relevant DOM elements and setup quick view functionality 
  */
  $(".carousel").on("init", function (e, slick) {
    tiles = document.querySelectorAll(".carousel .tile");

    // Activating any tile should launch the quick view modal
    tiles.forEach(function (tile) {
      tile.addEventListener("click", openDialog);
    });
  });

  /**
    Initialize Slick Slider with recommended configuration options
  */
  $(".carousel").slick({
    slidesToShow: 3,
    prevArrow:
      '<button class="previous-button is-control">' +
      '  <span class="fas fa-angle-left" aria-hidden="true"></span>' +
      '  <span class="sr-only">Previous slide</span>' +
      "</button>",
    nextArrow:
      '<button class="next-button is-control">' +
      '  <span class="fas fa-angle-right" aria-hidden="true"></span>' +
      '  <span class="sr-only">Next slide</span>' +
      "</button>",
    responsive: [
      {
        breakpoint: 575,
        settings: {
          slidesToShow: 2
        }
      },
      {
        breakpoint: 375,
        settings: {
          slidesToShow: 1
        }
      }
    ]
  });

  // Close the dialog when any of its interactive elements are activated
  dialogCloseButton.addEventListener("click", closeDialog);
  dialogOkButton.addEventListener("click", closeDialog);

  // Clicking anywhere outside the dialog content should close the dialog
  dialog.addEventListener("click", handleDialogClicks);
  dialog.addEventListener("keydown", handleDialogKeypresses);
});

/**
  NOTE: Modal dialog implementation for code demo purposes only!
*/
function openDialog(e) {
  e.preventDefault();
  triggeringElement = e.target;
  dialog.classList.remove("is-hidden");
  dialogCloseButton.focus();
}

function closeDialog() {
  triggeringElement.focus();
  dialog.classList.add("is-hidden");
}

function handleDialogClicks(e) {
  if (!dialogOverlay.contains(e.target)) {
    closeDialog();
  }
}

function handleDialogKeypresses(e) {
  switch (e.key) {
    case "Escape":
      closeDialog();
      break;

    case "Tab":
      if (e.shiftKey && document.activeElement === dialogCloseButton) {
        e.preventDefault();
        dialogOkButton.focus();
      } else if (!e.shiftKey && document.activeElement === dialogOkButton) {
        e.preventDefault();
        dialogCloseButton.focus();
      }

      break;
  }
}
